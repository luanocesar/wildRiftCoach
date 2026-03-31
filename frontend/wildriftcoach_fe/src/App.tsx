import { useState } from 'react'
import { UserOutlined } from '@ant-design/icons'
import { Button, Input, Space, Card } from 'antd'

import './App.css'

function App() {
  const [airesponse, setAIResponse] = useState("Ready.")
  const [championName, setChampionName] = useState("")

  const handleOnChange = (event:any)=>{
    setChampionName(event.target.value)
  }

  const handleOnClick = () => {
      const apiUrl = window.location.hostname === 'localhost' 
        ? 'http://localhost:8000/llm'
        : `${window.location.origin}/llm`;
      
      fetch(apiUrl,{
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ championName: championName }),
      })
      .then((res) => res.json())
      .then(
        (result) => {
          setAIResponse(result.response)
        },
        (error) => {
          console.error("Error fetching AI response:", error)
        }
      )
  }

  return (
    <>
      <Card title="Champion Build & Rune (By AI)" size="default">
      <p>{airesponse}</p>
    </Card>
      <Space direction="vertical" style={{ width: '100%' }}>
        <Input 
          onChange={handleOnChange} 
          prefix={<UserOutlined />} 
          placeholder="Enter champion name" 
          allowClear 
          onPressEnter={handleOnClick}
        />
        <Button onClick={handleOnClick} type="primary" block>Ask</Button>
      </Space>
    </>
  )
}

export default App