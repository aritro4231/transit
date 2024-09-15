import React, { useState } from 'react';
import { StyleSheet, Text, TextInput, Button, View, SafeAreaView, Alert } from 'react-native';


export const formedcreen = ({ navigation }) => {
    return (
        <View style={styles.container} >
            <Text> Welcome to UniRide! </Text>
            <Button>
                title = 'form'
                onPress = {() => navigation.navigate("home")}

            </Button>
        </View>
    )
}


