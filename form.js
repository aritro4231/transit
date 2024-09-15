import React, { useState } from 'react';
import { StyleSheet, Text, TextInput, Button, View, SafeAreaView, Alert } from 'react-native';

export default function App() {
    // State to hold form data
    const [name, setName] = useState('');
    const [age, setAge] = useState('');
    const [email, setEmail] = useState('');

    // Handle form submission
    const handleSubmit = () => {
        if (name && age && email) {
            Alert.alert("Form Submitted", `Name: ${name}, Age: ${age}, Email: ${email}`);
        } else {
            Alert.alert("Error", "Please fill in all fields.");
        }
    };

    return (
        <SafeAreaView style={styles.container}>
            <Text style={styles.header}>Fill out this form</Text>
            <Button>
                title = 'form'
                onPress = {() => navigation.navigate("home")}

            </Button>

            {/* Name Input */}
            <Text>Name:</Text>
            <TextInput
                style={styles.input}
                placeholder="Enter your name"
                value={name}
                onChangeText={setName}
            />

            {/* Age Input */}
            <Text>Age:</Text>
            <TextInput
                style={styles.input}
                placeholder="Enter your age"
                keyboardType="numeric"
                value={age}
                onChangeText={setAge}
            />

            {/* Email Input */}
            <Text>Email:</Text>
            <TextInput
                style={styles.input}
                placeholder="Enter your email"
                keyboardType="email-address"
                value={email}
                onChangeText={setEmail}
            />

            {/* Submit Button */}
            <Button title="Submit" onPress={handleSubmit} />
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 20,
    },
    header: {
        fontSize: 24,
        marginBottom: 20,
        textAlign: 'center',
    },
    input: {
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
        marginBottom: 20,
        borderRadius: 5,
    },
});
