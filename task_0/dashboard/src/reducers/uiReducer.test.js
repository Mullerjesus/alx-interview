import uiReducer from './uiReducer';

describe('uiReducer', () => {
    it('should return the initial state when no action is passed', () => {
        const initialState = {
            isNotificationDrawerVisible: false,
            isUserLoggedIn: false,
            user: {}
        };
        expect(uiReducer(undefined, {})).toEqual(initialState);
    });

    it('should handle DISPLAY_NOTIFICATION_DRAWER action', () => {
        const action = { type: 'DISPLAY_NOTIFICATION_DRAWER' };
        const expectedState = {
            isNotificationDrawerVisible: true,
            isUserLoggedIn: false,
            user: {}
        };
        expect(uiReducer(undefined, action)).toEqual(expectedState);
    });
});
