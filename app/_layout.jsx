import React, { useState } from 'react';
import { Text, View, Button, TextInput } from 'react-native';

export default function App() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');

  const handlePredict = async () => {
    try {
      const response = await fetch('http://localhost:5000/predict', {  // Update with your backend URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });
      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View>
      <TextInput
        value={input}
        onChangeText={setInput}
        placeholder="Enter input for AI"
      />
      <Button title="Predict" onPress={handlePredict} />
      <Text>Result: {result}</Text>
    </View>
  );
}
